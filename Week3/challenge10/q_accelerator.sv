// Q-Learning Accelerator
module q_accelerator #(
    parameter STATE_BITS = 4,    // bits to address states
    parameter ACTION_BITS = 2,   // bits to address actions
    parameter Q_WIDTH = 16        // width of Q-values (fixed-point)
)(
    input logic clk,
    input logic rst,
    input logic [STATE_BITS-1:0] current_state,
    input logic [ACTION_BITS-1:0] action,
    input logic [STATE_BITS-1:0] next_state,
    input logic [Q_WIDTH-1:0] reward,
    input logic [Q_WIDTH-1:0] gamma,     // discount factor (0 < gamma < 1)
    input logic update_enable,
    output logic [Q_WIDTH-1:0] updated_q_value
);

    // Assume small RAM to store Q-values
    logic [Q_WIDTH-1:0] q_table [0:(1<<STATE_BITS)-1][0:(1<<ACTION_BITS)-1];

    // Internal signals
    logic [Q_WIDTH-1:0] max_q_next;
    integer i;

    always_ff @(posedge clk or posedge rst) begin
        if (rst) begin
            // Initialize Q-table to zero
            for (i = 0; i < (1<<STATE_BITS); i = i + 1) begin
                q_table[i][0] <= 0;
                q_table[i][1] <= 0;
                q_table[i][2] <= 0;
                q_table[i][3] <= 0;
            end
        end else if (update_enable) begin
            // Find max(Q[next_state, all_actions])
            max_q_next = q_table[next_state][0];
            for (i = 1; i < (1<<ACTION_BITS); i = i + 1) begin
                if (q_table[next_state][i] > max_q_next) begin
                    max_q_next = q_table[next_state][i];
                end
            end

            // Q-learning Bellman Update:
            // Q(s,a) = Q(s,a) + alpha * (reward + gamma * max(Q(s',a')) - Q(s,a))
            q_table[current_state][action] <= reward + (gamma * max_q_next);
        end
    end

    // Output updated value
    assign updated_q_value = q_table[current_state][action];

endmodule
